.PHONY: tex clean

default: tex

TARGET := main.tex

tex:
	latexmk -pdf -silent -quiet $(TARGET)
clean:
	latexmk -CA
