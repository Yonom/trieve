import { Chunk, ChunkWithHighlights } from "../utils/types";
import React, { useCallback, useEffect, useRef } from "react";
import { ArrowIcon } from "./icons";

type Props = {
  item: ChunkWithHighlights;
  onResultClick: (chunk: Chunk & { position: number }) => void;
  showImages?: boolean;
  index: number;
  onUpOrDownClicked: (index: number, code: string) => void;
};

export const Item = ({
  item,
  onResultClick,
  showImages,
  index,
  onUpOrDownClicked,
}: Props) => {
  const Component = item.chunk.link ? "a" : "button";
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  const itemRef = useRef<HTMLButtonElement | HTMLLinkElement | any>(null);
  const title =
    item.chunk.metadata?.title ||
    item.chunk.metadata?.page_title ||
    item.chunk.metadata?.name;

  const checkForUpAndDown = useCallback(
    (e: KeyboardEvent) => {
      if (e.code === "ArrowDown" || e.code === "ArrowUp") {
        onUpOrDownClicked(index, e.code);
      }
    },
    [item]
  );

  useEffect(() => {
    itemRef.current?.addEventListener("keydown", checkForUpAndDown);
    return () => {
      itemRef.current?.removeEventListener("keydown", checkForUpAndDown);
    };
  }, []);

  return (
    <li>
      <Component
        ref={itemRef}
        id={`trieve-search-item-${index}`}
        className="item"
        onClick={() => onResultClick({ ...item.chunk, position: index })}
        {...(item.chunk.link ? { href: item.chunk.link } : {})}
      >
        <div>
          {showImages &&
          item.chunk.image_urls?.length &&
          item.chunk.image_urls[0] ? (
            <img src={item.chunk.image_urls[0]} />
          ) : null}
          {title ? (
            <div>
              <h4>{title}</h4>
              <p
                className="description"
                dangerouslySetInnerHTML={{ __html: item.highlights[0] }}
              />
            </div>
          ) : (
            <p
              dangerouslySetInnerHTML={{
                __html: item.highlights[0] || item.chunk.highlight || "",
              }}
            />
          )}
          <ArrowIcon />
        </div>
      </Component>
    </li>
  );
};
