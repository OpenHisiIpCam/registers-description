DOCGEN 	:= ./gen_docs.py

all: clean build generate

build:
	make -C ./hi3516av200
	make -C ./hi3520dv200

generate: build 
	$(DOCGEN)

clean:
	rm -f  ./*.rdl
	rm -rf ./output

deps:
	pip3 install ralbot-html
	pip3 install systemrdl-compiler
