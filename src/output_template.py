import typing


def first_output_type_func(
    flag: bool = False,
) -> typing.Optional[str]:
    
    if flag:
        return 'a'
    else:
        return None

def second_output_type_func() -> tuple[str, list, typing.Optional[int]]:
    return ('a', [], 1)

def third_output_type_func() -> tuple[str, list, typing.Optional[int]]:
    return 'a', [], None
