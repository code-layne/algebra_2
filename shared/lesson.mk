# shared/lesson.mk — included by every lesson-level Makefile.
# Auto-detects PROJECT_ROOT, UNIT, and LESSON from CURDIR.
#
# A component subdirectory may provide EITHER:
#   - main.tex  → compiled with latexmk to target/.../<comp>/main.pdf, or
#   - main.pdf  → a prefab PDF, used as-is straight from the source tree.
# Either form is discovered and merged into the packet by pdfunite.

PROJECT_ROOT := $(abspath ../..)
UNIT         := $(notdir $(abspath ..))
LESSON       := $(notdir $(CURDIR))

SHARED_STYS  := $(wildcard $(PROJECT_ROOT)/shared/*.sty)
TEXINPUTS    := $(PROJECT_ROOT)/shared//:
LATEXMK      = latexmk
LATEXFLAGS   = -xelatex \
               -interaction=nonstopmode \
               -halt-on-error \
               -file-line-error

STAMP_DIR    := $(PROJECT_ROOT)/.stamps/$(UNIT)/$(LESSON)
PDF_DIR      := $(PROJECT_ROOT)/target/$(UNIT)/$(LESSON)
COMPILED_DIR := $(PROJECT_ROOT)/target/compiled/$(UNIT)

# ── Component helpers ─────────────────────────────────────────────────────────
# A component "exists" if its directory holds a main.tex or a prefab main.pdf.
#   comp-present $1 → the dir name if usable, else empty
#   comp-pdf     $1 → the PDF to feed pdfunite: compiled target if main.tex,
#                     otherwise the source main.pdf used as-is
#   comp-stamp   $1 → a build stamp ONLY for tex components (prefab PDFs don't compile)
comp-present = $(if $(or $(wildcard $1/main.tex),$(wildcard $1/main.pdf)),$1)
comp-pdf     = $(if $(wildcard $1/main.tex),$(PDF_DIR)/$1/main.pdf,$1/main.pdf)
comp-stamp   = $(if $(wildcard $1/main.tex),$(STAMP_DIR)/$1/main.stamp)

# ── Component discovery (in pedagogical order) ────────────────────────────────
STUDENT_ORDER := cover warmup notes activity exit_ticket homework
KEYED_PAIRS   := warmup notes activity exit_ticket homework

STUDENT_COMPS := $(foreach c,$(STUDENT_ORDER),$(call comp-present,$(c)))
COVER_COMP    := $(call comp-present,cover)

# Full version: prefer <c>_key over the blank <c>; cover has no key.
KEYED_COMPS   := $(foreach c,$(KEYED_PAIRS),\
                   $(or $(call comp-present,$(c)_key),$(call comp-present,$(c))))
FULL_COMPS    := $(COVER_COMP) $(KEYED_COMPS)

# Key packet: the student packet with every blank component swapped for its key.
# Derived from STUDENT_COMPS (not KEYED_PAIRS) so the two packets pair up 1:1,
# component for component — that pairing is what lets the pagination pass give
# both packets identical page boundaries. A component with no _key sibling
# (cover) appears unchanged in both.
key-of        = $(or $(call comp-present,$1_key),$1)
KEY_COMPS     := $(foreach c,$(STUDENT_COMPS),$(call key-of,$(c)))

# Root lesson plan and slides may also be prefab PDFs.
HAS_ROOT      := $(or $(wildcard main.tex),$(wildcard main.pdf))
ROOT_STAMP    := $(if $(wildcard main.tex),$(STAMP_DIR)/main.stamp)
ROOT_PDF      := $(if $(HAS_ROOT),$(if $(wildcard main.tex),$(PDF_DIR)/main.pdf,main.pdf))

HAS_SLIDES    := $(call comp-present,slides)
SLIDES_STAMP  := $(call comp-stamp,slides)
SLIDES_PDF    := $(if $(HAS_SLIDES),$(call comp-pdf,slides))

# ── Stamp and PDF lists ───────────────────────────────────────────────────────
# Stamps drive compilation (tex only); PDF lists drive the pdfunite merge.
STUDENT_STAMPS := $(foreach c,$(STUDENT_COMPS),$(call comp-stamp,$(c)))
STUDENT_PDFS   := $(foreach c,$(STUDENT_COMPS),$(call comp-pdf,$(c)))

FULL_STAMPS    := $(ROOT_STAMP) $(SLIDES_STAMP) \
                  $(foreach c,$(FULL_COMPS),$(call comp-stamp,$(c)))
FULL_PDFS      := $(ROOT_PDF) $(SLIDES_PDF) \
                  $(foreach c,$(FULL_COMPS),$(call comp-pdf,$(c)))

KEY_STAMPS     := $(foreach c,$(KEY_COMPS),$(call comp-stamp,$(c)))
KEY_PDFS       := $(foreach c,$(KEY_COMPS),$(call comp-pdf,$(c)))

# Both packets are laid out against each other, so either target needs every
# component of both compiled before it can be paginated.
ALIGN_STAMPS   := $(sort $(STUDENT_STAMPS) $(KEY_STAMPS))

# ── Packet-wide pagination + recto starts + student/key alignment ─────────────
# Each component is its own document, so each numbers its pages from 1. After
# the merge, this pass rebuilds the packet so page numbers run across the whole
# document AND every component starts on an odd (right-hand) page: blank versos
# are inserted after a component that would otherwise leave the next one on a
# verso, including after the last, so the packet itself is even and one lesson
# never pushes the next one onto a verso. (unit.mk's own unit_cover/sample_test
# are NOT padded, so a unit packet is not recto-correct end to end.)
#
# The student and key packets are also kept page-for-page in step: each
# component occupies the SAME slot size in both — max(blank pages, key pages)
# rounded up to even — so page 7 of the key is page 7 of the student packet.
# The shorter of the two is padded with blank versos to fill its slot. Both
# targets compute the same slot sizes from the same two PDF lists, so they stay
# aligned whether built together or separately. See shared/paginate.tex.
#   $1 = merged PDF, rewritten in place.
#   $2 = the component PDFs that were merged, in the same order.
#   $3 = the counterpart packet's component PDFs, in the same order (1:1 with $2).
PAGINATE_DIR := $(PDF_DIR)/.paginate

define paginate
	@mkdir -p $(PAGINATE_DIR)
	@set -e; \
	set -- $3; \
	spec=; first=1; \
	for f in $2; do \
	  n=$$(pdfinfo "$$f" | awk '/^Pages/{print $$2}'); \
	  slot=$$n; \
	  if [ $$# -gt 0 ]; then \
	    m=$$(pdfinfo "$$1" | awk '/^Pages/{print $$2}'); \
	    shift; \
	    if [ $$m -gt $$slot ]; then slot=$$m; fi; \
	  fi; \
	  slot=$$(( (slot + 1) / 2 * 2 )); \
	  last=$$((first + n - 1)); \
	  spec="$$spec,$$first-$$last"; \
	  pad=$$((slot - n)); \
	  while [ $$pad -gt 0 ]; do spec="$$spec,{}"; pad=$$((pad - 1)); done; \
	  first=$$((last + 1)); \
	done; \
	spec=$${spec#,}; \
	TEXINPUTS="$(TEXINPUTS)" xelatex -interaction=nonstopmode -halt-on-error \
	    -output-directory="$(PAGINATE_DIR)" -jobname=paginated \
	    '\def\PacketSource{'"$1"'}\def\PacketPages{'"$$spec"'}\input{paginate}' \
	    > $(PAGINATE_DIR)/paginate.log 2>&1 \
	  && mv $(PAGINATE_DIR)/paginated.pdf $1 \
	  || { echo "!  pagination pass failed — see $(PAGINATE_DIR)/paginate.log"; \
	       grep -E "^(!|l\.)" $(PAGINATE_DIR)/paginate.log | head -10; exit 1; }
endef

# ── Targets ───────────────────────────────────────────────────────────────────
.PHONY: all student key full clean

all: student key full

student: $(ALIGN_STAMPS)
ifneq ($(strip $(STUDENT_PDFS)),)
	@mkdir -p $(COMPILED_DIR)
	pdfunite $(STUDENT_PDFS) $(COMPILED_DIR)/$(LESSON)_student.pdf
	$(call paginate,$(COMPILED_DIR)/$(LESSON)_student.pdf,$(STUDENT_PDFS),$(KEY_PDFS))
	@echo "✓  Student packet → target/compiled/$(UNIT)/$(LESSON)_student.pdf (paginated $(LESSON)-wide, components start recto)"
else
	@echo "  (no student components in $(UNIT)/$(LESSON))"
endif

key: $(ALIGN_STAMPS)
ifneq ($(strip $(KEY_PDFS)),)
	@mkdir -p $(COMPILED_DIR)
	pdfunite $(KEY_PDFS) $(COMPILED_DIR)/$(LESSON)_key.pdf
	$(call paginate,$(COMPILED_DIR)/$(LESSON)_key.pdf,$(KEY_PDFS),$(STUDENT_PDFS))
	@echo "✓  Key packet     → target/compiled/$(UNIT)/$(LESSON)_key.pdf (page-for-page with the student packet)"
else
	@echo "  (no keyed components in $(UNIT)/$(LESSON))"
endif

full: $(FULL_STAMPS)
ifneq ($(strip $(FULL_PDFS)),)
	@mkdir -p $(COMPILED_DIR)
	pdfunite $(FULL_PDFS) $(COMPILED_DIR)/$(LESSON)_full.pdf
	@echo "✓  Full lesson     → target/compiled/$(UNIT)/$(LESSON)_full.pdf"
else
	@echo "  (no content in $(UNIT)/$(LESSON))"
endif

# ── Pattern rule: compile a component subdirectory (tex components only) ───────
$(STAMP_DIR)/%/main.stamp: %/main.tex $(SHARED_STYS)
	@mkdir -p $(dir $@) $(PDF_DIR)/$*
	cd $* && TEXINPUTS="$(TEXINPUTS)" $(LATEXMK) $(LATEXFLAGS) \
		-outdir="$(PDF_DIR)/$*" main.tex
	@touch $@

# ── Rule: compile root-level main.tex ────────────────────────────────────────
$(STAMP_DIR)/main.stamp: main.tex $(SHARED_STYS)
	@mkdir -p $(dir $@) $(PDF_DIR)
	TEXINPUTS="$(TEXINPUTS)" $(LATEXMK) $(LATEXFLAGS) \
		-outdir="$(PDF_DIR)" main.tex
	@touch $@

clean:
	rm -rf $(STAMP_DIR) $(PDF_DIR)
	rm -f $(COMPILED_DIR)/$(LESSON)_student.pdf $(COMPILED_DIR)/$(LESSON)_key.pdf \
	      $(COMPILED_DIR)/$(LESSON)_full.pdf