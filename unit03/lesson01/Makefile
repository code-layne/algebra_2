include ../../shared/lesson.mk

# graded_sample/ is a graded quiz (grading.sty) kept OUT of the student and key
# packets: it builds only on request, so no packet changes.
#   make graded_sample       blank + key PDFs, manifest.json, blank/key check
#   make graded_sample_eval  also the 12 personalized copies for the invented
#                            class in graded_sample/eval/fake-roster.csv, then
#                            regenerates the synthetic scanned class set there
GRADED_EVAL := graded_sample/eval

.PHONY: graded_sample graded_sample_eval
graded_sample:
	@$(MAKE) --no-print-directory graded COMP=graded_sample

graded_sample_eval: graded_sample
	@$(MAKE) --no-print-directory roster-packets COMP=graded_sample ROSTER=$(GRADED_EVAL)/fake-roster.csv
	python3 $(GRADED_EVAL)/generate_eval.py
