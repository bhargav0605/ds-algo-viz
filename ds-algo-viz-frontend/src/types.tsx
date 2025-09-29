export type RandomRequest = {
    type: "random";
    cmd: "generate";
    minSize: number;
    maxSize: number;
    minRange: number;
    maxRange: number;
    sorting: string;
};

export type ServerResponse = {
    type: string;
    cmd: string;
    array?: number[];
    sorting?: string;
    minSize?: number;
    maxSize?: number;
    minRange?: number;
    maxRange?: number;
    i?: number;
    j?: number;
    [k: string]: unknown;
};