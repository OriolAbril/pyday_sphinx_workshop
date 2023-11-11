# Sample blogpost

:::{post} 5 Nov, 2023
:author: Oriol Abril Pla
:tags: sample, markdown, myst, blogging
:category: experiences, open source
:::

This is a sample blogpost that will be used to populate tag and category fields for the blog
generator. At the same time, we can also use it to showcase some of its capabilities already
at this point.

## Markdown support
Posts like this one can be written in markdown, and all its main features are supported

* lists
* tables

  | index | metadata | data |
  |-------|----------|------|
  | 0     |        A |  2.3 |
  | 1     |        B |  4.5 |
  | 2     |        A |  3.4 |
  | 3     |        A |  9.7 |

* code blocks

  ```python
  print("hello world, I'm blogging with syntax highlight!")
  ```

* links and images
* and more

## MyST
In fact, markdown support is available because we use the myst-parser extension, so what we really
have is myst support, with myst being a superset of markdown. We can use sphinx roles and directives
from markdown. As we have set up the intersphinx extension too, we can use cross-references:

|  source                | rendered |
|---|---|
| ``{func}`numpy.einsum` ``   | {func}`numpy.einsum` |
| ``{class}`str` ``              | {class}`str` |
| ``{term}`hashable` ``  | {term}`hashable`

We also have math support:

$$\hat{y} \sim \mathcal{N}(\mu, \sigma^2)$$

and use of any directive, like admonitions or tabs (from `sphinx-design`):

:::::{tab-set}
::::{tab-item} Source
```none
:::{note}
This is a note admonition
:::
```
::::
::::{tab-item} Rendered
:::{note}
This is a note admonition
:::
::::
:::::
