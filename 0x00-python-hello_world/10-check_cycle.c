#include "lists.h"
/**
 * check_cycle - cycle start and repeat
 * @list: pointer to head
 * Return: 1 on success, 0 otherwise.
 */
int check_cycle(listint_t *list)
{
listint_t *start;
listint_t *repeat;
if (list == NULL)
return (0);
start = list;
repeat = list;
while (repeat->next != NULL && repeat->next->next != NULL)
{
start = start->next;
repeat = repeat->next->next;
if (start == repeat)
{
start = list;
while (start != repeat)
{
start = start->next;
repeat = repeat->next;
}
return (1);
}
}
return (0);
}
