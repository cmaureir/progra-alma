#!/bin/bash

for page in $(find _build -name '*.html')
do
    #perl -p -i -e 's{`(.*?)`$}{<b>\1</b>}g;' $page
    perl -p -i -e 's{`(.*?)`}{<b>\1</b>}g;' $page
    perl -p -i -e 's{<p>Correct:</p>}{<p><font color="green">Correct:</font></p>}g' $page
    perl -p -i -e 's{<p>Wrong:</p>}{<p><font color="red">Wrong:</font></p>}g' $page
done

