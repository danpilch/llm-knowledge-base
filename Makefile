APP_NAME = agno-knowledge-base
APP_VSN ?= $(shell git rev-parse --short HEAD)

.PHONY: help
help: #: Show this help message
	@echo "$(APP_NAME):$(APP_VSN)"
	@awk '/^[A-Za-z_ -]*:.*#:/ {printf("%c[1;32m%-15s%c[0m", 27, $$1, 27); for(i=3; i<=NF; i++) { printf("%s ", $$i); } printf("\n"); }' Makefile* | sort

### Dev

.PHONY: run
run: #: Run the application
	python agent.py

### Docker
.PHONY: start-pgvector
start-pgvector: #: Start an existing pgvector datastore docker container 
start-pgvector:
	docker start pgvector

.PHONY: create-pgvector
create-pgvector: #: Create the pgvector datastore docker container 
create-pgvector:
	docker run -d \
  		-e POSTGRES_DB=ai \
		-e POSTGRES_USER=ai \
  		-e POSTGRES_PASSWORD=ai \
  		-e PGDATA=/var/lib/postgresql/data/pgdata \
  		-v pgvolume:/var/lib/postgresql/data \
  		-p 5532:5432 \
  		--name pgvector \
  		agnohq/pgvector:16

.PHONY: destroy-pgvector
destroy-pgvector: #: Destroy the pgvector datastore docker container 
destroy-pgvector:
	docker stop pgvector
	docker rm pgvector

.PHONY: create-pgvector-dimensions
create-pgvector-dimensions: #: Update pgvector table and document vectors for an existing table
create-pgvector-dimensions:
	python index_knowledge.py --create

.PHONY: upsert-pgvector-dimensions
upsert-pgvector-dimensions: #: Update pgvector table and document vectors for an existing table
upsert-pgvector-dimensions:
	python index_knowledge.py --upsert
