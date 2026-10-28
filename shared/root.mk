# shared/root.mk — included by the project-root Makefile.
# Delegates to the unit sub-makes and stitches the whole-curriculum packets.
#
# Only the student and key packets aggregate to this level. Each lesson's other
# three products (plan, the 3-up slides PDF, the full-page slides PPTX) stay in
# target/compiled/unitXX/ — they are per-lesson teacher artifacts.
#
# Grading, from the root:
#   make roster-packets LESSON=unit03/lesson01 ROSTER=~/Mathematics/rosters/roster-map.csv [SECTION=…]
#   make roster-packets COMP=unit02/tests/actual_test ROSTER=… [SECTION=…]   (a test or quiz)
#   make manifest COMP=unit03/lesson01/homework   (or COMP=unit02/tests/actual_test)

COMPILED_DIR := target/compiled
UNITS := $(patsubst %/Makefile,%,$(sort $(wildcard unit*/Makefile)))

.PHONY: all student key clean distclean check-names manifest roster-packets $(UNITS)

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

# Every graded document in the course (lessons and tests, blank and key): fails
# on any name line. `make manifest` runs the same check for one component.
check-names:
	@python3 shared/check_namelines.py $(UNITS)

# LESSON (unitXX/lessonYY) or COMP (unitXX/<path below the unit>) names what to
# build; the call goes to that unit's Makefile, which hands it on. ROSTER may
# start with ~/ and may be relative to this directory.
ROSTER_ABS = $(abspath $(patsubst ~/%,$(HOME)/%,$(ROSTER)))
GRADING_TARGET_PATH = $(patsubst %/,%,$(or $(LESSON),$(COMP)))
GRADING_UNIT = $(firstword $(subst /, ,$(GRADING_TARGET_PATH)))
GRADING_REST = $(patsubst $(GRADING_UNIT)/%,%,$(GRADING_TARGET_PATH))

manifest roster-packets:
	@test -n "$(GRADING_TARGET_PATH)" || { echo "!  set LESSON=unitXX/lessonYY (roster-packets) or COMP=unitXX/<component>, e.g."; \
	  echo "     make roster-packets LESSON=unit03/lesson01 ROSTER=~/Mathematics/rosters/roster-map.csv"; \
	  echo "     make manifest COMP=unit03/lesson01/homework"; exit 1; }
	@test "$(GRADING_REST)" != "$(GRADING_TARGET_PATH)" -a -f "$(GRADING_UNIT)/Makefile" \
	  || { echo "!  $(GRADING_TARGET_PATH) is not unitXX/<something> with a unit Makefile"; exit 1; }
	@$(MAKE) --no-print-directory -C $(GRADING_UNIT) $@ $(if $(LESSON),LESSON,COMP)=$(GRADING_REST) \
	    $(if $(ROSTER),ROSTER="$(ROSTER_ABS)") $(if $(SECTION),SECTION="$(SECTION)")

clean:
	@for u in $(UNITS); do $(MAKE) -C $$u clean; done
	rm -f $(COMPILED_DIR)/curriculum_student.pdf $(COMPILED_DIR)/curriculum_key.pdf \
	      $(COMPILED_DIR)/curriculum_full.pdf

distclean: clean
	rm -rf target .stamps
