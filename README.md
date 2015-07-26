# Webb

Webb is a script for managing web applications based on GNOME's Epiphany web browser,
which is now simply known as [Web] (https://wiki.gnome.org/Apps/Web). It makes creating and managing these applications
fairly easy and accessible via the Terminal. Just use this:

  ` webb -i webapp1 webapp2 ...`

  ` webb -r webapp1 webapp2 ...`

NEVER run this script as `root`. In order to have the latest version of Webb, run the following command
on your Terminal:

  ` curl https://rohan62442.github.io/Webb/webb-updater -o webb-updater && chmod +x webb-updater && ./webb-updater`

## Contributing workflow

Here’s how I suggest you go about proposing a change to this project:

1. [Fork this project][fork] to your account.
2. [Create a branch][branch] for the change you intend to make.
3. Make your changes to your fork.
4. [Send a pull request][pr] from your fork’s branch to my `master` branch.

Using the web-based interface to make changes is fine too, and will help you
by automatically forking the project and prompting to send a pull request too.

[fork]: http://help.github.com/forking/
[branch]: https://help.github.com/articles/creating-and-deleting-branches-within-your-repository
[pr]: http://help.github.com/pull-requests/

Please submit bugs and feature requests [here] (https://github.com/Rohan62442/Webb/issues).

You can have a look at the project [wiki] (https://github.com/Rohan62442/Webb/wiki) and [site] (http://rohan62442.github.io/Webb/). You can get in touch with me on [Twitter] (https://twitter.com/Rohan62442) and [Google+] (https://plus.google.com/+RohanPinto29/posts?hl=en). If you liked `Webb`, do promote it.

## License

[GNU General Public License v3](./COPYING)
