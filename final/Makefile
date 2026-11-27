# final/Makefile — course-level exam materials (not a unit; root.mk does not visit it).
#   make -C final            build the Mid-Year Final study guide
# The study guide is built exactly the way shared/unit.mk builds a unit study guide.
PROJECT_ROOT := $(abspath ..)
COMPILED_DIR := $(PROJECT_ROOT)/target/compiled

.PHONY: all study_guide clean

all: study_guide

study_guide:
	@mkdir -p $(COMPILED_DIR)/final
	cd study_guide && TEXINPUTS="$(PROJECT_ROOT)/shared//:$(PROJECT_ROOT)/math-shared:" \
	    latexmk -xelatex -interaction=nonstopmode -halt-on-error -file-line-error \
	    -outdir="$(PROJECT_ROOT)/target/final/study_guide" main.tex
	cp $(PROJECT_ROOT)/target/final/study_guide/main.pdf $(COMPILED_DIR)/final/midyear_final_study_guide.pdf
	@echo "✓  Study guide       → target/compiled/final/midyear_final_study_guide.pdf"

clean:
	rm -rf $(PROJECT_ROOT)/target/final $(COMPILED_DIR)/final
