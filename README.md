# cal-notebooks
CEOS Analytics Laboratory notebooks and tools

## Contributing

Contributions are welcome.

A `pre-commit` hook is provided in `/bin`. For each notebook committed this will strip *outputs* from the notebook to reduce the size of the repository.

The `apply_hooks.sh` script creates a symlink to `bin/pre-commit`.

```bash
# Run this in your local repository
sh bin/apply_hooks.sh
```

For contributors:

1. Apply the pre-commit hook.
1. Run each notebook (that has been updated) to populate the figures, tables and other *outputs* as you want them.
1. `git add` and `git commit`.
1. If eveything looks ok, `git push` to your fork of this repository and create a *pull request*.
