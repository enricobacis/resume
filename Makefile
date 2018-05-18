.PHONY   : all clean fresh serve test

SOURCE   = resume.json
THEME    = slick
HTML     = html/index.html

all: $(HTML)

$(HTML): $(SOURCE)
	resume export $@ --theme $(THEME) --format html
	html/makehtml.py $@ $@

clean:
	@ find . -name 'resume*' -and -not -name '*.json' -exec rm '{}' \+
	@ rm -f $(HTML)

fresh: | clean all

serve: | fresh
	@ cd html; ./serve.py

test: $(SOURCE)
	resume test $@
