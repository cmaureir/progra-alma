src=report

all:
	@rubber -d $(src)

clean:
	rm -f $(src).{aux,log,bbl,blg,out}
	rm -f  src/*.{aux,log}
distclean: clean 
	rm -f $(src).pdf
x:
	okular $(src).pdf &> /dev/null &
