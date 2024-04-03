from typing import overload

import groq
import instructor


@overload
def from_groq(
    client: groq.Groq,
    mode: instructor.Mode = instructor.Mode.TOOLS,
    **kwargs,
) -> instructor.Instructor: ...


@overload
def from_groq(
    client: groq.Groq,
    mode: instructor.Mode = instructor.Mode.TOOLS,
    **kwargs,
) -> instructor.Instructor: ...


def from_groq(
    client: groq.Groq,
    mode: instructor.Mode = instructor.Mode.TOOLS,
    **kwargs,
) -> instructor.Instructor:
    assert mode in {
        instructor.Mode.JSON,
        instructor.Mode.TOOLS,
    }, "Mode be one of {instructor.Mode.JSON, instructor.Mode.TOOLS}"

    assert isinstance(client, (groq.Groq)), "Client must be an instance of groq.GROQ"

    if isinstance(client, groq.Groq):
        return instructor.Instructor(
            client=client,
            create=instructor.patch(create=client.chat.completions.create, mode=mode),
            provider=instructor.Provider.GROQ,
            mode=mode,
            **kwargs,
        )

    else:
        return instructor.Instructor(
            client=client,
            create=instructor.patch(create=client.messages.create, mode=mode),
            provider=instructor.Provider.GROQ,
            mode=mode,
            **kwargs,
        )