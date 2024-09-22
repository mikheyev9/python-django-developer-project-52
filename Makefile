USER_NAME=$(shell whoami)
STATIC_DIR=/var/www/project/static
MEDIA_DIR=/var/www/project/media

setup-directories:
	@echo "Creating static and media directories..."
	@bash -c 'echo "Введите пароль для sudo:" && read -s PASSWORD && \
	echo $$PASSWORD | sudo -S mkdir -p $(STATIC_DIR) $(MEDIA_DIR) && \
	echo $$PASSWORD | sudo -S chown -R $(USER_NAME):$(USER_NAME) $(STATIC_DIR) $(MEDIA_DIR) && \
	echo $$PASSWORD | sudo -S chmod -R 755 $(STATIC_DIR) $(MEDIA_DIR)'
	@echo "Directories and permissions set up!"

setup-directories-root:
	@echo "Creating static and media directories..."
	@mkdir -p $(STATIC_DIR) $(MEDIA_DIR)
	@chown -R $(USER_NAME):$(USER_NAME) $(STATIC_DIR) $(MEDIA_DIR)
	@chmod -R 755 $(STATIC_DIR) $(MEDIA_DIR)
	@echo "Directories and permissions set up!"

