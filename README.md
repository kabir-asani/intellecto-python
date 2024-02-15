# intellecto-python

A wrapper around Hugging Face's Inference API (written in Python)

## Usage

**Sync Version**

```python
from intellecto import Intellecto

client = Intellecto(
    access_token="xxxxxxxxxxxxxxxxxxxxxxxxxxxx"
)

response = client.nlp.generate(
    model="microsoft/phi-2",
    input='Top 10 programming languages in the world.'
)
```

**Async Version**

```python
from asyncio import run
from intellecto import AsyncIntellecto

client = AsyncIntellecto(
    access_token="xxxxxxxxxxxxxxxxxxxxxxxxxxxx"
)

async def main() -> None:
    response = await client.nlp.client.nlp.generate(
        model="microsoft/phi-2",
        input='Top 10 programming languages in the world.'
    )

run(main())
```

## Exposed APIs

### `Intellecto`

`Intellecto` has the following properties --

| property | description                                                                        |
| -------- | ---------------------------------------------------------------------------------- |
| nlp      | A property of type `IntellectoNLP` that deals with various NLP related tasks       |
| audio    | A property of type `IntellectoAudio` that deals with various audio related tasks   |
| vision   | A property of type `IntellectoVision` that deals with various vision related tasks |

### `AsyncIntellecto`

`AsyncIntellecto` has the following properties --

| property | description                                                                             |
| -------- | --------------------------------------------------------------------------------------- |
| nlp      | A property of type `AsyncIntellectoNLP` that deals with various NLP related tasks       |
| audio    | A property of type `AsyncIntellectoAudio` that deals with various audio related tasks   |
| vision   | A property of type `AsyncIntellectoVision` that deals with various vision related tasks |

---

## Code Structure

### `IntellectoBase`

`IntellectoBase` spawns and holds onto a `IntellectoClient` which aids it in sending network requests to Inference API end points.

It receives the following parameters -

| parameter | description                                       |
| --------- | ------------------------------------------------- |
| `model`   | A `<model-id>` as specified on HF's model page    |
| `token`   | A `<bearer-token>` as extracted from HF's console |

`IntellectoBase` is extended by the classes mentioned below. They're divided & grouped as per their niche and tasks.

1. [`IntellectoNLP`](https://huggingface.co/docs/api-inference/en/detailed_parameters#natural-language-processing)

    - [`fill`](https://huggingface.co/docs/api-inference/en/detailed_parameters#fill-mask-task)
    - [`summarise`](https://huggingface.co/docs/api-inference/en/detailed_parameters#summarization-task)
    - [`qna`](https://huggingface.co/docs/api-inference/en/detailed_parameters#question-answering-task)
    - [`table`](https://huggingface.co/docs/api-inference/en/detailed_parameters#table-question-answering-task)
    - [`similarity`](https://huggingface.co/docs/api-inference/en/detailed_parameters#sentence-similarity-task)
    - [`classify`](https://huggingface.co/docs/api-inference/en/detailed_parameters#text-classification-task)
    - [`generate`](https://huggingface.co/docs/api-inference/en/detailed_parameters#text-generation-task)
    - [`recognise`](https://huggingface.co/docs/api-inference/en/detailed_parameters#token-classification-task)
    - [`translate`](https://huggingface.co/docs/api-inference/en/detailed_parameters#translation-task)
    - [`zero_shot_classify`](https://huggingface.co/docs/api-inference/en/detailed_parameters#zero-shot-classification-task)
    - [`conversational`](https://huggingface.co/docs/api-inference/en/detailed_parameters#conversational-task)
    - [`feature_extract`](https://huggingface.co/docs/api-inference/en/detailed_parameters#feature-extraction-task)

2. [`IntellectoAudio`](https://huggingface.co/docs/api-inference/en/detailed_parameters#audio)

    - [`transcribe`](https://huggingface.co/docs/api-inference/en/detailed_parameters#automatic-speech-recognition-task)
    - [`classify`](https://huggingface.co/docs/api-inference/en/detailed_parameters#audio-classification-task)

3. [`IntellectoVision`](https://huggingface.co/docs/api-inference/en/detailed_parameters#computer-vision)
    - [`classify`](https://huggingface.co/docs/api-inference/en/detailed_parameters#image-classification-task)
    - [`detect`](https://huggingface.co/docs/api-inference/en/detailed_parameters#object-detection-task)

### `AsyncIntellectoBase`

`AsyncIntellectoBase` spawns and holds onto an `AsyncIntellectoClient` which aids it in sending network requests to Inference API end points.

It receives the following parameters -

| parameter | description                                       |
| --------- | ------------------------------------------------- |
| `model`   | A `<model-id>` as specified on HF's model page    |
| `token`   | A `<bearer-token>` as extracted from HF's console |

`AsyncIntellectoBase` is extended by the classes mentioned below. They're divided & grouped as per their niche and tasks.

1. [`AsyncIntellectoNLP`](https://huggingface.co/docs/api-inference/en/detailed_parameters#natural-language-processing)

    - [`fill`](https://huggingface.co/docs/api-inference/en/detailed_parameters#fill-mask-task)
    - [`summarise`](https://huggingface.co/docs/api-inference/en/detailed_parameters#summarization-task)
    - [`qna`](https://huggingface.co/docs/api-inference/en/detailed_parameters#question-answering-task)
    - [`table`](https://huggingface.co/docs/api-inference/en/detailed_parameters#table-question-answering-task)
    - [`similarity`](https://huggingface.co/docs/api-inference/en/detailed_parameters#sentence-similarity-task)
    - [`classify`](https://huggingface.co/docs/api-inference/en/detailed_parameters#text-classification-task)
    - [`generate`](https://huggingface.co/docs/api-inference/en/detailed_parameters#text-generation-task)
    - [`recognise`](https://huggingface.co/docs/api-inference/en/detailed_parameters#token-classification-task)
    - [`translate`](https://huggingface.co/docs/api-inference/en/detailed_parameters#translation-task)
    - [`zero_shot_classify`](https://huggingface.co/docs/api-inference/en/detailed_parameters#zero-shot-classification-task)
    - [`conversational`](https://huggingface.co/docs/api-inference/en/detailed_parameters#conversational-task)
    - [`feature_extract`](https://huggingface.co/docs/api-inference/en/detailed_parameters#feature-extraction-task)

2. [`AsyncIntellectoAudio`](https://huggingface.co/docs/api-inference/en/detailed_parameters#audio)

    - [`transcribe`](https://huggingface.co/docs/api-inference/en/detailed_parameters#automatic-speech-recognition-task)
    - [`classify`](https://huggingface.co/docs/api-inference/en/detailed_parameters#audio-classification-task)

3. [`AsyncIntellectoVision`](https://huggingface.co/docs/api-inference/en/detailed_parameters#computer-vision)
    - [`classify`](https://huggingface.co/docs/api-inference/en/detailed_parameters#image-classification-task)
    - [`detect`](https://huggingface.co/docs/api-inference/en/detailed_parameters#object-detection-task)

## Handling Errors

When the library is unable to connect to the API (for example, due to network connection problems or a timeout), a subclass of `IntellectoAPIError` is raised.

When the API returns a non-success status code (that is, 4xx or 5xx response), a subclass of `IntellectoAPIStatusError` is raised, containing `status_code`.

Error codes are as followed:

| Status Code | Error Type                 |
| ----------- | -------------------------- |
| 400         | `BadRequestError`          |
| 401         | `AuthenticationError`      |
| 403         | `PermissionDeniedError`    |
| 404         | `NotFoundError`            |
| 422         | `UnprocessableEntityError` |
| 429         | `RateLimitError`           |
| 5xx         | `InternalServerError`      |
| N/A         | `APIConnectionError`       |
