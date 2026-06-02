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

# ── Lesson 1 component lists ──────────────────────────────────────────────────
L01 := target/unit01/lesson01

L01_STUDENT_STAMPS := \
    .stamps/unit01/lesson01/cover/main.stamp \
    .stamps/unit01/lesson01/warmup/main.stamp \
    .stamps/unit01/lesson01/notes/main.stamp \
    .stamps/unit01/lesson01/activity/main.stamp \
    .stamps/unit01/lesson01/exit_ticket/main.stamp \
    .stamps/unit01/lesson01/homework/main.stamp

L01_STUDENT_PDFS := \
    $(L01)/cover/main.pdf \
    $(L01)/warmup/main.pdf \
    $(L01)/notes/main.pdf \
    $(L01)/activity/main.pdf \
    $(L01)/exit_ticket/main.pdf \
    $(L01)/homework/main.pdf

L01_FULL_STAMPS := \
    .stamps/unit01/lesson01/main.stamp \
    .stamps/unit01/lesson01/slides/main.stamp \
    .stamps/unit01/lesson01/cover/main.stamp \
    .stamps/unit01/lesson01/warmup/main.stamp \
    .stamps/unit01/lesson01/warmup_key/main.stamp \
    .stamps/unit01/lesson01/notes/main.stamp \
    .stamps/unit01/lesson01/notes_key/main.stamp \
    .stamps/unit01/lesson01/activity/main.stamp \
    .stamps/unit01/lesson01/activity_key/main.stamp \
    .stamps/unit01/lesson01/exit_ticket/main.stamp \
    .stamps/unit01/lesson01/exit_ticket_key/main.stamp \
    .stamps/unit01/lesson01/homework/main.stamp \
    .stamps/unit01/lesson01/homework_key/main.stamp

L01_FULL_PDFS := \
    $(L01)/main.pdf \
    $(L01)/slides/main.pdf \
    $(L01)/cover/main.pdf \
    $(L01)/warmup/main.pdf \
    $(L01)/warmup_key/main.pdf \
    $(L01)/notes/main.pdf \
    $(L01)/notes_key/main.pdf \
    $(L01)/activity/main.pdf \
    $(L01)/activity_key/main.pdf \
    $(L01)/exit_ticket/main.pdf \
    $(L01)/exit_ticket_key/main.pdf \
    $(L01)/homework/main.pdf \
    $(L01)/homework_key/main.pdf

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
