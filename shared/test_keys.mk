# shared/test_keys.mk — build a unit's summative assessment answer keys.
# Included by each unitNN/test_keys/Makefile (`include ../../shared/test_keys.mk`).
# Every subdirectory holding a main.tex compiles to target/<unit>/test_keys/<name>/main.pdf.

PROJECT_ROOT := $(abspath ../..)
UNIT         := $(notdir $(abspath ..))
TEXINPUTS    := $(PROJECT_ROOT)/shared//:$(PROJECT_ROOT)/math-shared:
# A clone updated from before math-shared moved to the project root keeps the
# old submodule checkout in shared/common (git leaves it behind). shared//
# would then find its example main.tex files ahead of a component's own.
$(if $(wildcard $(PROJECT_ROOT)/shared/common/*),$(error shared/common is the old math-shared checkout; remove it: rm -rf "$(PROJECT_ROOT)/shared/common" && git submodule update --init))
PDF_DIR      := $(PROJECT_ROOT)/target/$(UNIT)/test_keys
LATEXFLAGS   := -xelatex -interaction=nonstopmode -halt-on-error -file-line-error

KEYS := $(patsubst %/main.tex,%,$(wildcard */main.tex))

# The practice test key doubles as the unit "sample test key" drop-in: its compiled
# PDF is published to ../sample_test_key/main.pdf, which shared/unit.mk merges into
# the FULL packet only. The actual test key is never published into a packet.
DROP_SRC := practice_test_key
DROP_DST := ../sample_test_key/main.pdf

.PHONY: all clean drop $(KEYS)

all: $(KEYS) drop

$(KEYS):
	@mkdir -p $(PDF_DIR)/$@
	cd $@ && TEXINPUTS="$(TEXINPUTS)" latexmk $(LATEXFLAGS) \
	    -outdir="$(PDF_DIR)/$@" main.tex
	@echo "OK  $(UNIT) test key -> target/$(UNIT)/test_keys/$@/main.pdf"

drop: $(DROP_SRC)
	@mkdir -p $(dir $(DROP_DST))
	cp $(PDF_DIR)/$(DROP_SRC)/main.pdf $(DROP_DST)
	@echo "OK  Published practice test key -> $(UNIT)/sample_test_key/main.pdf (full packet)"

clean:
	rm -rf $(PDF_DIR)
