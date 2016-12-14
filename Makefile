.PHONY   : all clean fresh test

SOURCE   = resume.json
THEME    = slick

all: resume.html

resume.html: $(SOURCE)
	resume export $@ --theme $(THEME)
	python makehtml.py $@ $@

clean:
	@ find . -name 'resume*' -and -not -name '*.json' -exec rm '{}' \+

fresh: | clean all

test: $(SOURCE)
	resume test $@
