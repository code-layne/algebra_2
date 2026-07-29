# shared/root.mk — included by the project-root Makefile.
# Delegates to the unit sub-makes and stitches the whole-curriculum packets.
#
# Only the student and key packets aggregate to this level. Each lesson's other
# three products (plan, slides PDF, slides PPTX) stay in
# target/compiled/unitXX/ — they are per-lesson teacher artifacts.

COMPILED_DIR := target/compiled
UNITS := $(patsubst %/Makefile,%,$(sort $(wildcard unit*/Makefile)))

.PHONY: all student key clean distclean $(UNITS)

all: $(UNITS)

$(UNITS):
	$(MAKE) -C $@

student:
	@for u in $(UNITS); do $(MAKE) -C $$u student || exit 1; done
	@mkdir -p $(COMPILED_DIR)
	@pdfs=$$(ls $(COMPILED_DIR)/unit*_student.pdf 2>/dev/null | sort); \
	if [ -n "$$pdfs" ]; then \
	  pdfunite $$pdfs $(COMPILED_DIR)/curriculum_student.pdf; \
	  echo "✓  Curriculum student → target/compiled/curriculum_student.pdf"; \
	fi

key:
	@for u in $(UNITS); do $(MAKE) -C $$u key || exit 1; done
	@mkdir -p $(COMPILED_DIR)
	@pdfs=$$(ls $(COMPILED_DIR)/unit*_key.pdf 2>/dev/null | sort); \
	if [ -n "$$pdfs" ]; then \
	  pdfunite $$pdfs $(COMPILED_DIR)/curriculum_key.pdf; \
	  echo "✓  Curriculum key     → target/compiled/curriculum_key.pdf"; \
	fi

clean:
	@for u in $(UNITS); do $(MAKE) -C $$u clean; done
	rm -f $(COMPILED_DIR)/curriculum_student.pdf $(COMPILED_DIR)/curriculum_key.pdf \
	      $(COMPILED_DIR)/curriculum_full.pdf

distclean: clean
	rm -rf target .stamps
