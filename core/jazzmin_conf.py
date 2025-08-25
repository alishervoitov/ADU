JAZZMIN_SETTINGS = {
    "site_title": "ADU Admin",
    "site_header": "ADU",
    "site_brand": "ADU",
    "site_logo": "books/img/logo.png",
    "site_logo_classes": "img-circle",
    "welcome_sign": "ADU boshqaruv paneliga xush kelibsiz!",
    "copyright": "ADU University",
    "search_model": ["users.User", "common.FrontendTranslation", "structure.Employee", "structure.Faculty", "structure.Department", "structure.Divisions", "structure.MenuItem"],
    "user_avatar": None,

    ############
    # Top Menu #
    ############

    "topmenu_links": [
        {"name": "Bosh sahifa",  "url": "admin:index", "permissions": ["auth.view_user"]},
        {"name": "Yordam", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},
        {"model": "users.User"},
        {"app": "structure"},
    ],

    #############
    # User Menu #
    #############

    "usermenu_links": [
        {"name": "Yordam", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},
        {"model": "users.User"}
    ],

    #############
    # Side Menu #
    #############

    "show_sidebar": True,
    "navigation_expanded": True,
    "hide_apps": [],
    "hide_models": [],
    "order_with_respect_to": [
        "structure",
        "structure.Faculty",
        "structure.Department",
        "structure.Specialty",
        "structure.Employee",
        "structure.Divisions",
        "structure.MenuItem",
        "structure.Document",
        "structure.HomePageText",
        "structure.UniversityBaseInfo",
        "blog",
        "users",
        "auth",
    ],
    "custom_links": {},
    "icons": {
        "structure": "fas fa-university",
        "structure.Faculty": "fas fa-building-columns",
        "structure.Department": "fas fa-sitemap",
        "structure.Specialty": "fas fa-graduation-cap",
        "structure.Employee": "fas fa-user-tie",
        "structure.Divisions": "fas fa-layer-group",
        "structure.MenuItem": "fas fa-bars",
        "structure.Document": "fas fa-file-alt",
        "structure.HomePageText": "fas fa-home",
        "structure.UniversityBaseInfo": "fas fa-info-circle",
        "users": "fas fa-users",
        "auth": "fas fa-users-cog",
        "users.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "blog": "fas fa-blog",
        "blog.FAQ": "fas fa-question-circle",
        "blog.InteractiveService": "fas fa-cogs",
    },
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",


    #################
    # Related Modal #
    #################

    "related_modal_active": False,

    #############
    # UI Tweaks #
    #############
    "custom_css": None,
    "custom_js": None,
    "use_google_fonts_cdn": True,
    "show_ui_builder": True,

    ###############
    # Change view #
    ###############
    # Render out the change view as a single form, or in tabs, current options are
    # - single
    # - horizontal_tabs (default)
    # - vertical_tabs
    # - collapsible
    # - carousel
    "changeform_format": "horizontal_tabs",
    # override change forms on a per modeladmin basis
    "changeform_format_overrides": {"auth.user": "collapsible", "auth.group": "vertical_tabs"},
    # Add a language dropdown into the admin
    "language_chooser": True,
}