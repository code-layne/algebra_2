.PHONY: all clean distclean unit00 unit01

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
UNIT01_MAINS   := $(shell find unit01_foundations -name main.tex | sort)
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

# ── Cleanup ───────────────────────────────────────────────────────────────────
clean:
	rm -rf target .stamps

distclean: clean
