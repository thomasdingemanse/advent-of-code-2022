#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define A 65
#define Z 90
#define a 97
#define z 122
#define nothing '\n'

int find_duplicate_item(char * backpack, size_t len) {
    char * items;
    size_t n_items;
    int present;

    items = malloc(len);
    n_items = 0;

    /* First compartment */
    for(size_t i = 0; i < len / 2; ++i) {
        present = 0;

        /* Check if we already encountered this item in the 1st compartment */
        for (size_t j = 0; j < n_items; j++) {
            if (items[j] == backpack[i]) {
                present = 1;
                break;
            }
        }

        /* Add to items of 1st compartment if it's not already there */
        if (!present) {
            items[n_items] = backpack[i];
            n_items++;
        }
    }

    /* Second compartment */
    for(size_t i = len / 2; i < len; ++i) {
        
        /* Check if this item was also in the first compartment */
        for (size_t j = 0; j < n_items; j++) {
            if (items[j] == backpack[i]) {
                return backpack[i];
            }
        }
    }

    free(items);
}

int item_priority(char c) {
    /* Uppercase letter: priority 27-52 */
    if (A <= c && c <= Z) {
        return c - 38;
    }

    /* Lowercase letter: priority 1-26 */
    if (a <= c && c <= z) {
        return c - 96;
    }
}

void list_item_types(char * backpack, char * list, int items_found) {
    char priority;
    
    /* List the priority of each item this elf carries. */
    for(size_t item = 0; item < items_found; ++item) {
        priority = (char) item_priority(backpack[item]);

        list[priority] = 1;
    }
}

void part1() {
    FILE * file = fopen("./input_heleen.txt", "r");
    char * backpack;
    size_t i, len, sum;
    char c, duplicate_item;
    int priority;
    
    backpack = malloc(1024);
    i = 0;
    len = 0;
    sum = 0;

    while ((c = fgetc(file)) != EOF)
    {
        if (c == '\n') {
            if (len > 0) {
                duplicate_item = find_duplicate_item(backpack, len);
                priority = item_priority(duplicate_item);

                // printf("Found the wrongly packed item! Priority %d\n", priority);

                sum += priority;
            }

            len = 0;
            i = 0;
        } else {
            len++;
            backpack[i] = (char) c;
            i++;
        }
    }

    free(backpack);

    printf("Sum: %ld\n", sum);
}

void part2() {
    FILE * file = fopen("./input_heleen.txt", "r");

    int elf = 1;
    int group = 1;

    char * backpack = malloc(1024);

    /* Keep track of how many of each item we have per group. */
    int total_item_types = 2 * 26;

    char list_of_first_elf[total_item_types + 1];
    char list_of_second_elf[total_item_types + 1];
    char list_of_third_elf[total_item_types + 1];

    int items_found = 0;
    
    char item;
    
    int priority;
    int total_priority = 0;

    memset(list_of_first_elf, 0, (total_item_types + 1));
    memset(list_of_second_elf, 0, (total_item_types + 1));
    memset(list_of_third_elf, 0, (total_item_types + 1));

    while ((item = fgetc(file)) != EOF)
    {
        /* The poor elf has completely emptied its backpack in the snow. */
        if (item == nothing) {

            if (items_found > 0) {

                /* All elves in the group make a list of all unique items they carry. */
                if (elf == 1) {

                    list_item_types(backpack, list_of_first_elf, items_found);

                } else if (elf == 2) {
                    
                    list_item_types(backpack, list_of_second_elf, items_found);

                /* The last elf of each group starts looking for the badge. */
                } else if (elf == 3) {

                    list_item_types(backpack, list_of_third_elf, items_found);

                    /* Check all items one by one to see which one we have three of. */
                    for (char item_type = 1; item_type <= total_item_types; ++item_type) {

                        // printf("Checking item with priority %d [1/3]\n", item_type);

                        if (list_of_first_elf[item_type] == 0) {
                            continue;
                        }
                        // printf("Checking item with priority %d [2/3]\n", item_type);
                        
                        if (list_of_second_elf[item_type] == 0) {
                            continue;
                        }
                        // printf("Checking item with priority %d [3/3]\n", item_type);
                        
                        if (list_of_third_elf[item_type] == 0) {
                            continue;
                        }

                        // printf("Found the badge! Priority %d\n", item_type);

                        /* Found the badge! */
                        total_priority += item_type;
                    }

                    printf("Group %d.\n", group);

                    /* Walk towards the next group of elves. */
                    elf = 0;
                    group++;

                    /* Forget all about this group of elves' hijinks. */
                    memset(list_of_first_elf, 0, (total_item_types + 1));
                    memset(list_of_second_elf, 0, (total_item_types + 1));
                    memset(list_of_third_elf, 0, (total_item_types + 1));
                }

                /* Examine the contents of the next elf's backpack. */
                items_found = 0;
                elf++;
            }

        } else {
            /* Found something! */
            backpack[items_found] = (char) item;
            items_found++;
        }
    }

    printf("Sum: %d\n", total_priority);

    free(backpack);
}

void main() {
    part1();
    part2();
}