# unit02/extras/Makefile — standalone one-off handouts (e.g. the parent-visit board problems). Merged
# into NO packet and NOT listed in shared/unit.mk or shared/root.mk (unit.mk globs lesson*/ only),
# so the unit's verified packets never reflow. Every subdirectory holding a main.tex compiles to
# target/<unit>/extras/<name>/main.pdf.

PROJECT_ROOT := $(abspath ../..)
UNIT         := $(notdir $(abspath ..))
TEXINPUTS    := $(PROJECT_ROOT)/shared//:$(PROJECT_ROOT)/math-shared:
# A clone updated from before math-shared moved to the project root keeps the
# old submodule checkout in shared/common (git leaves it behind). shared//
# would then find its example main.tex files ahead of a component's own.
$(if $(wildcard $(PROJECT_ROOT)/shared/common/*),$(error shared/common is the old math-shared checkout; remove it: rm -rf "$(PROJECT_ROOT)/shared/common" && git submodule update --init))
PDF_DIR      := $(PROJECT_ROOT)/target/$(UNIT)/extras
LATEXFLAGS   := -xelatex -interaction=nonstopmode -halt-on-error -file-line-error

EXTRAS := $(patsubst %/main.tex,%,$(wildcard */main.tex))

.PHONY: all clean $(EXTRAS)
all: $(EXTRAS)
$(EXTRAS):
	@mkdir -p $(PDF_DIR)/$@
	cd $@ && TEXINPUTS="$(TEXINPUTS)" latexmk $(LATEXFLAGS) -outdir="$(PDF_DIR)/$@" main.tex
	@echo "OK  $(UNIT) extras -> target/$(UNIT)/extras/$@/main.pdf"

clean:
	rm -rf $(PDF_DIR)
