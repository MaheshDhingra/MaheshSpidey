import { NextRequest, NextResponse } from 'next/server';
import path from 'path';
import fs from 'fs/promises';

const DATA_ROOT = path.resolve(process.cwd(), '../data');

export async function GET(req: NextRequest, context: { params: { path: string[] } }) {
  const relPath = context.params.path ? context.params.path.join('/') : '';
  const filePath = path.join(DATA_ROOT, relPath);

  try {
    const ext = path.extname(filePath);
    const file = await fs.readFile(filePath, 'utf-8');
    if (ext === '.json') {
      return NextResponse.json(JSON.parse(file));
    } else if (ext === '.csv') {
      // Simple CSV to JSON conversion
      const [header, ...rows] = file.split(/\r?\n/).filter(Boolean);
      const keys = header.split(',');
      const data = rows.map(row => {
        const values = row.split(',');
        return Object.fromEntries(keys.map((k, i) => [k, values[i]]));
      });
      return NextResponse.json(data);
    } else {
      return new NextResponse('Unsupported file type', { status: 415 });
    }
  } catch {
    return new NextResponse('File not found', { status: 404 });
  }
} 