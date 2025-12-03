GREEN  := \033[0;32m
YELLOW := \033[0;33m
RED    := \033[0;31m
NC     := \033[0m # No Color

IMAGE_NAME := uv-example
IMAGE_TAG := latest

.PHONY: wheel model build run clean help

# Default target
.DEFAULT_GOAL := help

help:
	@echo "$(YELLOW)Available targets:$(NC)"
	@echo "  $(GREEN)wheel$(NC)       - Build wheel if dist/ is empty"
	@echo "  $(GREEN)model$(NC)       - Trains model if not exists"
	@echo "  $(GREEN)build$(NC)       - Build docker if wheel + model exists"
	@echo "  $(GREEN)run$(NC)         - Run container in detached mode"
	@echo "  $(GREEN)test$(NC)        - curl localhost/health and fail loudly if not 200"

wheel:
	@echo "$(YELLOW)Building wheel $(IMAGE_NAME):$(IMAGE_TAG)$(NC)"
	@if [ -z "$(wildcard dist/slanggen-*.whl)" ]; then \
		echo "No wheel found... building"; \
		uv build --wheel; \
	else \
		echo "Wheel already exists: $(wildcard dist/slanggen-*.whl)"; \
	fi

model: wheel
	@echo "$(YELLOW)training model $(IMAGE_NAME):$(IMAGE_TAG)$(NC)"
	@if [ -z "$(wildcard artefacts/model.pth)" ]; then \
		echo "No model found... building"; \
		python src/slanggen/main.py; \
	else \
		echo "Model already exists: $(wildcard artefacts/model.pth)"; \
	fi

build: model
	@echo "$(YELLOW) building $(IMAGE_NAME):$(IMAGE_TAG)"
	docker build -t $(IMAGE_NAME):$(IMAGE_TAG) .
	@echo "$(GREEN)Build complete!$(NC)"

run: build
	@echo "$(YELLOW)Starting container $(IMAGE_NAME):$(IMAGE_TAG)...$(NC)"
	# adding the -t flag enables color codiding for loguru
	docker run -t -p 80:80 $(IMAGE_NAME):$(IMAGE_TAG)

clean:
	@echo "$(YELLOW)Cleaning up...$(NC)"
	-docker stop $(IMAGE_NAME) 2>/dev/null || true
	-docker rm $(IMAGE_NAME) 2>/dev/null || true
	-docker rmi $(IMAGE_NAME):$(IMAGE_TAG) 2>/dev/null || true
	@echo "$(GREEN)Cleanup complete!$(NC)"

