freeze:
	pip freeze > requirements.txt

main:
	python main.py

add:
	cd my_pinecone && python add_document.py
