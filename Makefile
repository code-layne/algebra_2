.PHONY: all clean distclean shared

LATEXMK = latexmk
LATEXFLAGS = -pdf \
              -interaction=nonstopmode \
              -halt-on-error \
              -file-line-error \
              -outdir=target/shared
SHARED_DIR = shared
SHARED_MAIN = lesson_template.tex
SHARED_OUT = target/$(SHARED_DIR)

all: shared

shared:
	mkdir -p $(SHARED_OUT)
	cd $(SHARED_DIR) && \
	$(LATEXMK) $(LATEXFLAGS) $(SHARED_MAIN)

clean:
	rm -rf target

distclean:
	rm -rf target