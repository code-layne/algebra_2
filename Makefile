.PHONY: all clean distclean shared unit00 unit01

LATEXMK = latexmk
LATEXFLAGS = -xelatex \
             -interaction=nonstopmode \
             -halt-on-error \
             -file-line-error

# recursively find all main.tex files
SHARED_MAINS := $(shell find shared -name main.tex)
UNIT00_MAINS := $(shell find unit00_introduction -name main.tex)
UNIT01_MAINS := $(shell find unit01_foundations -name main.tex)

ALL_MAINS := $(SHARED_MAINS) $(UNIT00_MAINS) $(UNIT01_MAINS)

all:
	@for tex in $(ALL_MAINS); do \
		dir=$$(dirname $$tex); \
		out=target/$$dir; \
		mkdir -p $$out; \
		echo "Building $$tex -> $$out"; \
		$(LATEXMK) $(LATEXFLAGS) -outdir=$$out $$tex; \
	done

clean:
	rm -rf target

distclean:
	rm -rf target