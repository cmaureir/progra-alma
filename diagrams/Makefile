TEXFILES = $(wildcard *.tex)
PDFFILES = $(TEXFILES:.tex=.pdf)
PNGFILES = $(PDFFILES:.pdf=.png)

all: png gif

png: $(PNGFILES)
pdf: $(PDFFILES)
gif: $(GIFFILES)

%.pdf: %.tex
	@rubber --pdf $<
%.png: %.pdf
	@echo "creating $@..."
	@convert -density 1200 -scale 10\% -quality 80 $< $@
	@convert -geometry 500 a6.svg a6.jpg
clean:
	@rubber --clean --pdf $(TEXFILES:.tex=)
	@rm -f *.png *.gif *.vrb

.PHONY: png pdf clean all

