.PHONY: tex \
	proof \
	clean

default: tex

TARGET := main.tex

tex:
	latexmk -pdf -silent -quiet $(TARGET)

# Check style:
proof:
	echo "weasel words: "
	./bin/weasel.sh *.tex
	echo
	echo "passive voice: "
	./bin/passive.sh *.tex
	echo
	echo "duplicates: "
	perl bin/dups.pl *.tex

clean:
	latexmk -CA
