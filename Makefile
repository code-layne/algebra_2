.PHONY: all clean distclean

LATEXMK = latexmk
LATEXFLAGS = -f -pdf -interaction=nonstopmode -halt-on-error -file-line-error

UNIT1_MAIN = unit1_foundations
UNIT1_TEX = $(UNIT1_MAIN)/**/*.tex

all: unit1

unit1: $(UNIT1_MAIN)
	mkdir -p target/$(UNIT1_MAIN)
	$(LATEXMK) $(LATEXFLAGS) -outdir=target/$(UNIT1_MAIN) $(UNIT1_TEX)

clean:
	$(LATEXMK) -c $(UNIT1_MAIN)
	rm -rf target

distclean:
	$(LATEXMK) -C $(UNIT1_MAIN)
	rm -rf target