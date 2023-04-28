### 1.16.0 (28.04.2023)

- `css_class` field added to menu item

### 1.15.0 (17.03.2023)

- Prefetching relations in `utils.get_menus`

### 1.14.0 (28.02.2023)

- Upgrade `garpix_page` to version 2.42.0.

### 1.14.0-rc1 (10.02.2023)

- Upgrade `garpix_page` to version 2.42.0-rc2.
- `subpage_url` parameter added.
- `MenuItemSerializer` updated.

### 1.13.0 (16.11.2022)

- Page in admin is using as `raw_id_fields`

### 1.12.0 - 1.12.1 (08.11.2022)

- MenuItem instance added to menu items in context processor (`object` key)
- `get_active_children` method added to MenuItem model.
- `MenuItemWithChildrenSerializer` serializer added.
- `is_current` and `is_current_full` values added to `MenuItemSerializer

### 1.11.0 (12.09.2022)
- Added file link

### 1.10.0 (16.08.2022)

- Clone object action to admin added
- Multisite support added to context processor

### 1.9.0 (29.06.2022)

- Multisite support added

### 1.8.0 (15.04.2022)

- Added hash on current page support

### 1.7.0 (11.01.2022)

- Added hash in LinkMixin

### 1.6.1-1.6.2 (08.11.2021)

- Bugfix icon.

### 1.6.0 (29.10.2021)

- Added icon.
- Added settings.py variable `MENU_ICON_ALLOWED_TYPES`.
- Added settings.py variable `MENU_ICON_MAX_SIZE`.

### 1.5.1 (19.09.2021)

- Removed elements from model_to_dict :)

### 1.5.0 (19.09.2021)

- Added `is_current` and `is_current_full`.

### 1.4.0 (19.09.2021)

- Utils for SPA menus.

### 1.3.0 (19.09.2021)

- Used model_to_dict for menu_processor.

### 1.2.0 (18.09.2021)

- Added `mixins.LinkMixin` (for `garpix_page` and external urls).

### 1.1.0 (08.09.2021)

- Added the ability to filter active_manager for the MenuItem model

### 1.0.2 (20.07.2021)

- Fixed bug with `'NoneType' object has no attribute 'startswith'`.

### 1.0.1 (17.07.2021)

- Fixed bug with `get_link()`.

### 1.0.0 (06.05.2021)

- First release in pypi.org.
