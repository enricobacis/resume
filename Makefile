SOURCE   = resume.json
THEME    = slick

resume.html: $(SOURCE)
	resume export $@ -t $(THEME)
