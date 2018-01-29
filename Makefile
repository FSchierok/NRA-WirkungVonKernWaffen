all: build/WirkungVonKernwaffen.pdf

texoptions = \
	     --lualatex \
			 --interaction=nonstopmode \
		   --halt-on-error \
		   --output-directory=build

build/WirkungVonKernwaffen.pdf: FORCE img/over.pdf img/fried.pdf | build
	latexmk	$(texoptions)	main.tex
	mv build/main.pdf build/WirkungVonKernwaffen.pdf

build/thesen_Wirkung_von_Kerwaffen.pdf: FORCE | build
	latexmk	$(texoptions)	thesen_Wirkung_von_Kerwaffen.tex

img/over.pdf:
	python plot.py

img/fried.pdf:
	python plot.py

build:
	mkdir -p build

clean:
	rm -r build

FORCE:

.PHONY:	all clean
