# shared/tests.mk — build a unit's summative assessments (blank student copies).
# Included by each unitNN/tests/Makefile (`include ../../shared/tests.mk`).
# Every subdirectory holding a main.tex compiles to target/<unit>/tests/<name>/main.pdf.

PROJECT_ROOT := $(abspath ../..)
UNIT         := $(notdir $(abspath ..))
TEXINPUTS    := $(PROJECT_ROOT)/shared//:$(PROJECT_ROOT)/math-shared:
# A clone updated from before math-shared moved to the project root keeps the
# old submodule checkout in shared/common (git leaves it behind). shared//
# would then find its example main.tex files ahead of a component's own.
$(if $(wildcard $(PROJECT_ROOT)/shared/common/*),$(error shared/common is the old math-shared checkout; remove it: rm -rf "$(PROJECT_ROOT)/shared/common" && git submodule update --init))
PDF_DIR      := $(PROJECT_ROOT)/target/$(UNIT)/tests
LATEXFLAGS   := -xelatex -interaction=nonstopmode -halt-on-error -file-line-error

TESTS := $(patsubst %/main.tex,%,$(wildcard */main.tex))

# The practice test doubles as the unit "sample test" drop-in: its compiled PDF is
# published to ../sample_test/main.pdf, which shared/unit.mk merges into BOTH the
# student and full packets. The actual test is never published into a packet.
DROP_SRC := practice_test
DROP_DST := ../sample_test/main.pdf

.PHONY: all clean drop $(TESTS)

all: $(TESTS) drop

$(TESTS):
	@mkdir -p $(PDF_DIR)/$@
	cd $@ && TEXINPUTS="$(TEXINPUTS)" latexmk $(LATEXFLAGS) \
	    -outdir="$(PDF_DIR)/$@" main.tex
	@echo "OK  $(UNIT) test -> target/$(UNIT)/tests/$@/main.pdf"

drop: $(DROP_SRC)
	@mkdir -p $(dir $(DROP_DST))
	cp $(PDF_DIR)/$(DROP_SRC)/main.pdf $(DROP_DST)
	@echo "OK  Published practice test -> $(UNIT)/sample_test/main.pdf (student + full packet)"

clean:
	rm -rf $(PDF_DIR)

# ── Grading (math-shared, the submodule at the project root) ──────────────────
# Every quiz and test here is graded (\gradedblank), and its key is
# ../test_keys/<name>_key.
#
#   make manifest COMP=factoring_quiz
#       blank + key builds, target/<unit>/tests/grading/<COMP>/manifest.json,
#       and the check that the blank and key agree on every graded item.
#   make roster-packets COMP=factoring_quiz ROSTER=~/Rosters/algebra2/roster-map.csv [SECTION=…]
#       one run per student, in roster order, joined into
#       target/compiled/<unit>/<COMP>_roster.pdf to print as one collated job:
#       math-shared's cover sheet (the only page with her name), its blank back,
#       then her personalized copy (tracking id in the QR codes and the "ID:"
#       strip) padded to an even page count — math-shared's grading-personalized
#       output as it stands. It fails if any roster name reaches a graded page.
#
# The cover sheets and the roster PDF carry student names: they stay under
# target/, which is never committed. Included last, so `all` stays the default.
GRADING_MK    := $(PROJECT_ROOT)/math-shared/grading.mk
COMP          ?=
COMPONENT     := $(COMP)
KEY_COMPONENT := ../test_keys/$(COMP)_key
GRADING_OUT   := $(PDF_DIR)/grading/$(COMP)
ROSTER_OUT    := $(PROJECT_ROOT)/target/compiled/$(UNIT)/$(COMP)_roster.pdf

.PHONY: manifest roster-packets grading-need-comp

ifneq ($(wildcard $(GRADING_MK)),)
include $(GRADING_MK)

grading-need-comp:
	@test -n "$(COMP)" || { echo "!  set COMP=<test directory>, e.g. COMP=$(firstword $(TESTS))"; exit 1; }

manifest: grading-need-comp
	@$(MAKE) --no-print-directory grading-manifest
	@echo "OK  Manifest -> target/$(UNIT)/tests/grading/$(COMP)/manifest.json"

roster-packets: grading-need-comp grading-need-roster
	@$(MAKE) --no-print-directory grading-personalized
	@mkdir -p $(dir $(ROSTER_OUT))
	@cp $(GR_OUT)/personalized.pdf $(ROSTER_OUT)
	@echo "OK  Roster packets -> target/compiled/$(UNIT)/$(COMP)_roster.pdf (roster order, cover sheet first)"
else
manifest roster-packets grading-need-comp:
	@echo "!  math-shared is empty — run: git submodule update --init"; exit 1
endif
