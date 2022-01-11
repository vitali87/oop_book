from collections import Hashable
from typing import Union, Iterable, Tuple, Any, Mapping, Dict, cast

DictInit=Union[
    Iterable[
        Tuple[
            Hashable,Any
        ]
    ],
    Mapping[Hashable, Any]
]

class NoDupDict(Dict[Hashable,Any]):
    def __setitem__(self, key: Hashable, value: Any) -> None:
        if key in self:
            raise ValueError(f"duplicate {key!r}")
        super().__setitem__(key,value)

    def __init__(self, init: DictInit = None,
                 **kwargs: Any) -> None:
        if (
            isinstance(init, Mapping)
            or not isinstance(init, Iterable)
            and init is not None
        ):
            super().__init__(init, **kwargs)
        elif isinstance(init, Iterable):
            for k,v in cast(Iterable[Tuple[Hashable,Any]], init):
                self[k] = v
        else:
            super().__init__(**kwargs)