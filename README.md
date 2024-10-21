# TODO

## Embeddings:
- [FAILED] Try to give instruction to instructor-xl embedding model (failed due to latency in library update)


## Tree Sitter
- [TODO] Add comments to tree splitter
- [TODO] Add import statements to tree splitter
- [TODO] Add metadata for types of codes, then use it in the vector search functionality

## Parser
- [Done] Use token as chunk unit, instead of characters - Token size of 20 ~ 30 seems to perform well
- [Done] Tried LLama Index's CodeSplitter, which specifies huge chunk size - does not perform well because it make up words like GS = Google Server: https://docs.sweep.dev/blogs/chunking-improvements
- [TODO] Try CintraAI Code Chunker: https://github.com/CintraAI/code-chunker



## Memory
- https://python.langchain.com/v0.1/docs/modules/memory/types/summary/
- Semantic Caching: [semantic cache](https://www.mongodb.com/developer/products/atlas/advanced-rag-langchain-mongodb/)

## Contextual Retreiver
- Convert Chunk to Contextualized Chunk
- Embeddings => Contextual Embeddings
- BM25 index => Contextual BM25
```
original_chunk = "The company's revenue grew by 3% over the previous quarter."

contextualized_chunk = "This chunk is from an SEC filing on ACME corp's performance in Q2 2023; the previous quarter's revenue was $314 million. The company's revenue grew by 3% over the previous quarter."
```


## LightRAG



## Qdrant