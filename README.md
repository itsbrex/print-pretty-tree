# Print Pretty Tree

a.k.a. `ptree` is a simple Python script that displays the directory tree of the current working directory with color-coded output for easy file identification.

<p align="center">
  <img width="460"  src="https://i.imgur.com/GSO6vmJ.jpg">
</p>

## Installation

To install `print-pretty-tree`, you can use either `pip` or other package managers like `npm`, `pnpm`, or `yarn`.

### Install using pip

If you have Python and `pip` installed:

```bash
pip install print-pretty-tree --user
```

### Install using other package managers

If you have `npm` 5.2 or higher, we recommend using `npx` to run packages globally. This way, you don't need to install the package globally and can still use it as a tool.

```bash
npx print-pretty-tree
```

If you still want to install `print-pretty-tree` globally, on the command line, run the following command:

```bash
npm install -g print-pretty-tree
```

If you get an EACCES permissions error, you may need to reinstall `npm` with a version manager or manually change `npm`'s default directory. For more information, see the [npm docs here](https://docs.npmjs.com/resolving-eacces-permissions-errors-when-installing-packages-globally).

## Usage

Once you have installed `print-pretty-tree`, you can run the script in any directory.
> You can run any of the commands below in any directory, regardless of how you installed it.
```bash
pt

ptree

print-pretty-tree
```

The script excludes certain files and folders like node_modules and .git by default to make the output easier to manage. It will recursively display the directory structure in a visually pleasing way.

## Local Development
```bash
# clone the repo
git clone https://github.com/itsbrex/print-pretty-tree.git

# cd into the repo
cd print-pretty-tree

# build the package
python3 -m build
```

## Customization

- To add more file types and colors to the output, you can modify the `FILE_TYPE_COLORS` dictionary in the script.
- You can also customize the excluded file patterns by modifying the `EXCLUDED_PATTERNS` list in the script.

## Contributing

If you find any bugs or want to suggest new features, please feel free to contribute by submitting an [issue](https://github.com/itsbrex/print-pretty-tree/issues) or a [pull request](https://github.com/itsbrex/print-pretty-tree/pulls).

## Contributors ✨
Thanks goes to these wonderful people ([emoji key](https://github.com/all-contributors/all-contributors#emoji-key)):

<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/github/all-contributors/itsbrex/print-pretty-tree?color=ee8449&style=flat-square)](#Contributing)

<!-- ALL-CONTRIBUTORS-BADGE:END -->

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->
This project follows the [all-contributors](https://allcontributors.org/) specification. Contributions of any kind welcome!

## License

Licensed under the MIT license. See the [LICENSE](./LICENSE) file for more information.

If you found this project interesting or helpful, please consider [sponsoring me](https://github.com/sponsors/itsbrex) or <a href="https://twitter.com/itsbrex">following me on twitter <img src="https://storage.googleapis.com/saasify-assets/twitter-logo.svg" alt="twitter" height="24px" align="center"></a>