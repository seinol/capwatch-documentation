# Update Translations

```bash
make gettext
sphinx-intl update -p _build/gettext -l de
# edit updated files in locales/de/LC_MESSAGES/
```

For more information, take a look at the [Sphinx documentation on i18n](http://www.sphinx-doc.org/en/master/usage/advanced/intl.html).
