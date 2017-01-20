# Python change directory with searching

This is a simple program designed to save time when changing directories via command line.

## The problem

Something that I always find as an issue when using command line is that a lot of the time when swapping directories in terminal is having to constantly tab until i get to the directory i want.

If I know the directory i'm looking for is '~/some_repo/src/main/java/co/uk/something/', the usual course of action is to go ~/som(TAB)/src/m(TAB), which gets tedious after having to do it all the time.

## The solution

My idea of a solution was to do a regex search on whatever the string was after the final /.

So the solution to the above could be something like '~/some_repo/somet.+', which would take me to the directory I stated above.

## Issues with the solution

There are some issues with the solution that will likely have to say this way. Notably, it takes the first match and changes to that directory to save time, as otherwise this could take forever if you wanted to effectively search and find every possible 'log' folder in the file system's root, for example.

This ends up being part issue in some folders, such as when you have multiple 'src' directories in a project. In the end though, these are usually still faster than the alternative as you'd likely just narrow your search by changing into a directory you're more sure of not having collisions.

Notably it's also *very slightly* slower when changing to an existing directory. Not really noticeable though, and likely won't be a problem in terms of productivity.

# Requirements

* Python3 (tested on 3.5.2)

## Additional requirements

The default bin creates a command called 'dir_search'. This will only print out the matched directory, so if you want to use this to change directories you will require a bash alias, as such:

```bash
function change_dir(){
    cd "$(dir_search "$1")"
}
alias scd='change_dir'
#alias cd='change_dir' (for people who are happy with relying on it!!)
```


