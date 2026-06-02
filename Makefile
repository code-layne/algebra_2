.PHONY: all clean distclean unit00 unit01 lesson01-student lesson01-full

PROJECT_ROOT := $(CURDIR)
TEXINPUTS    := $(PROJECT_ROOT)/shared//:

LATEXMK      = latexmk
LATEXFLAGS   = -xelatex \
               -interaction=nonstopmode \
               -halt-on-error \
               -file-line-error

# ── Source discovery ──────────────────────────────────────────────────────────
SHARED_STYS    := $(wildcard shared/*.sty)
UNIT00_MAINS   := $(shell find unit00_introduction -name main.tex | sort)
UNIT01_MAINS   := $(shell find unit01 -name main.tex | sort)
ALL_MAINS      := $(UNIT01_MAINS)

# ── Stamp paths (mirror source tree under .stamps/) ───────────────────────────
UNIT00_STAMPS  := $(patsubst %.tex, .stamps/%.stamp, $(UNIT00_MAINS))
UNIT01_STAMPS  := $(patsubst %.tex, .stamps/%.stamp, $(UNIT01_MAINS))
ALL_STAMPS     := $(UNIT01_STAMPS)

# ── PDF paths derived from source paths ───────────────────────────────────────
UNIT00_PDFS    := $(patsubst %.tex, target/%.pdf, $(UNIT00_MAINS))
UNIT01_PDFS    := $(patsubst %.tex, target/%.pdf, $(UNIT01_MAINS))

# ── Default target ────────────────────────────────────────────────────────────
all: $(ALL_STAMPS)

# ── Pattern rule: one main.tex → one stamp ────────────────────────────────────
.stamps/%.stamp: %.tex $(SHARED_STYS)
	@mkdir -p $(dir $@) target/$(dir $*)
	cd $(dir $<) && \
		TEXINPUTS="$(TEXINPUTS)" \
		$(LATEXMK) $(LATEXFLAGS) \
		-outdir="$(PROJECT_ROOT)/target/$(dir $<)" main.tex
	@touch $@

# ── Unit bundle targets ───────────────────────────────────────────────────────
unit00: $(UNIT00_STAMPS)
	mkdir -p target/compiled
	pdfunite $(UNIT00_PDFS) target/compiled/unit00.pdf
	@echo "✓  Unit 00  →  target/compiled/unit00.pdf"

unit01: $(UNIT01_STAMPS)
	mkdir -p target/compiled
	pdfunite $(UNIT01_PDFS) target/compiled/unit01.pdf
	@echo "✓  Unit 01  →  target/compiled/unit01.pdf"

# ── Helpers for mixed compiled/pre-built components ───────────────────────────
# If a subdir has main.tex → use the compiled PDF from target/.
# If a subdir has only pre-built PDFs → use them directly from source.
compiled_pdf  = $(if $(wildcard $(1)/main.tex),target/$(1)/main.pdf,$(wildcard $(1)/*.pdf))
compiled_stamp = $(if $(wildcard $(1)/main.tex),.stamps/$(1)/main.stamp,)

# ── Lesson 1 component lists ──────────────────────────────────────────────────
L01_DIRS_STUDENT := \
    unit01/lesson01/cover \
    unit01/lesson01/warmup \
    unit01/lesson01/notes \
    unit01/lesson01/activity \
    unit01/lesson01/exit_ticket \
    unit01/lesson01/homework

L01_DIRS_FULL := \
    unit01/lesson01 \
    unit01/lesson01/slides \
    unit01/lesson01/cover \
    unit01/lesson01/warmup \
    unit01/lesson01/warmup_key \
    unit01/lesson01/notes \
    unit01/lesson01/notes_key \
    unit01/lesson01/activity \
    unit01/lesson01/activity_key \
    unit01/lesson01/exit_ticket \
    unit01/lesson01/exit_ticket_key \
    unit01/lesson01/homework \
    unit01/lesson01/homework_key

L01_STUDENT_STAMPS := $(foreach d,$(L01_DIRS_STUDENT),$(call compiled_stamp,$(d)))
L01_STUDENT_PDFS   := $(foreach d,$(L01_DIRS_STUDENT),$(call compiled_pdf,$(d)))

L01_FULL_STAMPS    := $(foreach d,$(L01_DIRS_FULL),$(call compiled_stamp,$(d)))
L01_FULL_PDFS      := $(foreach d,$(L01_DIRS_FULL),$(call compiled_pdf,$(d)))

lesson01-student: $(L01_STUDENT_STAMPS)
	mkdir -p target/compiled
	pdfunite $(L01_STUDENT_PDFS) target/compiled/unit01_lesson01_student.pdf
	@echo "✓  Student packet  →  target/compiled/unit01_lesson01_student.pdf"

lesson01-full: $(L01_FULL_STAMPS)
	mkdir -p target/compiled
	pdfunite $(L01_FULL_PDFS) target/compiled/unit01_lesson01_full.pdf
	@echo "✓  Full lesson     →  target/compiled/unit01_lesson01_full.pdf"

# ── Cleanup ───────────────────────────────────────────────────────────────────
clean:
	rm -rf target .stamps

distclean: clean
