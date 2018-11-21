.PHONY   : all clean fresh html serve test

SOURCE   = resume.json
HTML     = html/index.html

all: $(HTML)

$(HTML): $(SOURCE) node_modules
	resume serve &
	sleep 10 && pkill -f "resume serve"
	mv public/index.html $(HTML)
	html/makehtml.py $(HTML) $(HTML)

node_modules:
	npm install

clean:
	@ rm -rf node_modules package-lock.json
	@ find . -name 'resume*' -and -not -name '*.json' -and -not -name '*.template' -exec rm '{}' \+
	@ rm -f $(HTML)

fresh: | clean all

serve:
	resume serve

test: $(SOURCE)
	resume test $@
