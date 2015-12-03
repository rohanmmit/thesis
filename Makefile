.PHONY: tex clean

default: tex

TARGET := main.tex

tex:
	pdflatex $(TARGET)
clean:
	latexmk -CA
