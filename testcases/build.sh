#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

cd $DIR/how2heap
make
mv $DIR/how2heap/{fastbin_dup,fastbin_dup_into_stack,unsafe_unlink,house_of_spirit,poison_null_byte,malloc_playground,first_fit,house_of_lore,overlapping_chunks,overlapping_chunks_2,house_of_force,unsorted_bin_attack,house_of_einherjar,house_of_orange} $DIR/bin

for i in `ls $DIR/src`; do
    gcc -g -o $DIR/bin/${i%.*} $DIR/src/$i
done
