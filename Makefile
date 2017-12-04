all: build/WirkungVonKernwaffen.pdf

texoptions = \
	     --lualatex \
			 --interaction=nonstopmode \
		   --halt-on-error \
		   --output-directory=build

build/WirkungVonKernwaffen.pdf: FORCE | build
	latexmk	$(texoptions)	main.tex
	mv build/main.pdf build/WirkungVonKernwaffen.pdf

build:
	mkdir -p build

clean:
	rm -r build

FORCE:

.PHONY:	all clean
