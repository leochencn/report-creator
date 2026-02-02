#!/usr/bin/env python3
"""
LaTeX Beamer 编译脚本
用于将.tex文件编译为PDF，支持中文（使用xelatex）
"""

import subprocess
import sys
import os
import argparse
from pathlib import Path


def compile_latex(tex_file: str, output_dir: str = None, verbose: bool = False) -> bool:
    """
    编译LaTeX文件为PDF
    
    Args:
        tex_file: .tex文件路径
        output_dir: 输出目录（可选）
        verbose: 是否显示详细输出
    
    Returns:
        bool: 编译是否成功
    """
    tex_path = Path(tex_file).resolve()
    
    if not tex_path.exists():
        print(f"错误：文件不存在 {tex_file}", file=sys.stderr)
        return False
    
    if not tex_path.suffix == '.tex':
        print(f"错误：文件必须是.tex格式 {tex_file}", file=sys.stderr)
        return False
    
    # 设置工作目录为tex文件所在目录
    work_dir = tex_path.parent
    tex_name = tex_path.name
    
    # 确定输出目录
    if output_dir:
        out_dir = Path(output_dir).resolve()
        out_dir.mkdir(parents=True, exist_ok=True)
    else:
        out_dir = work_dir
    
    # 编译命令参数
    cmd = [
        'xelatex',
        '-interaction=nonstopmode',
        '-file-line-error',
        f'-output-directory={out_dir}',
        tex_name
    ]
    
    print(f"正在编译: {tex_file}")
    print(f"工作目录: {work_dir}")
    print(f"输出目录: {out_dir}")
    
    # 第一次编译
    print("\n[1/2] 第一次编译...")
    try:
        result = subprocess.run(
            cmd,
            cwd=work_dir,
            capture_output=not verbose,
            text=True,
            encoding='utf-8',
            errors='ignore'
        )
        
        if result.returncode != 0 and not verbose:
            print("编译警告（可能是引用未解析，继续第二次编译）")
            if result.stderr:
                print(result.stderr[:500])  # 显示前500字符错误信息
    
    except FileNotFoundError:
        print("错误：未找到xelatex，请确保已安装TeX Live或MiKTeX", file=sys.stderr)
        return False
    except Exception as e:
        print(f"编译出错: {e}", file=sys.stderr)
        return False
    
    # 第二次编译（用于正确生成目录和引用）
    print("\n[2/2] 第二次编译（解析引用）...")
    try:
        result = subprocess.run(
            cmd,
            cwd=work_dir,
            capture_output=not verbose,
            text=True,
            encoding='utf-8',
            errors='ignore'
        )
        
        if result.returncode != 0:
            print(f"编译失败，返回码: {result.returncode}", file=sys.stderr)
            if not verbose and result.stderr:
                print("错误信息:", file=sys.stderr)
                print(result.stderr[:1000], file=sys.stderr)
            return False
        
    except Exception as e:
        print(f"编译出错: {e}", file=sys.stderr)
        return False
    
    # 检查PDF是否生成
    pdf_name = tex_path.stem + '.pdf'
    pdf_path = out_dir / pdf_name
    
    if pdf_path.exists():
        print(f"\n✓ 编译成功！")
        print(f"PDF文件: {pdf_path}")
        print(f"文件大小: {pdf_path.stat().st_size / 1024:.1f} KB")
        return True
    else:
        print(f"\n✗ 编译可能失败，未找到PDF文件", file=sys.stderr)
        return False


def clean_auxiliary_files(tex_file: str, output_dir: str = None) -> None:
    """
    清理编译生成的辅助文件
    
    Args:
        tex_file: .tex文件路径
        output_dir: 输出目录（可选）
    """
    tex_path = Path(tex_file).resolve()
    stem = tex_path.stem
    
    if output_dir:
        work_dir = Path(output_dir).resolve()
    else:
        work_dir = tex_path.parent
    
    # 辅助文件扩展名
    aux_extensions = [
        '.aux', '.log', '.nav', '.out', '.snm', '.toc',
        '.vrb', '.synctex.gz', '.fdb_latexmk', '.fls'
    ]
    
    cleaned = []
    for ext in aux_extensions:
        aux_file = work_dir / (stem + ext)
        if aux_file.exists():
            aux_file.unlink()
            cleaned.append(aux_file.name)
    
    if cleaned:
        print(f"已清理辅助文件: {', '.join(cleaned)}")


def main():
    parser = argparse.ArgumentParser(
        description='编译LaTeX Beamer文件为PDF（支持中文）',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
示例:
  python compile_beamer.py report.tex
  python compile_beamer.py report.tex -o output/
  python compile_beamer.py report.tex -v
  python compile_beamer.py report.tex --clean
        '''
    )
    
    parser.add_argument('tex_file', help='LaTeX源文件(.tex)')
    parser.add_argument('-o', '--output', dest='output_dir',
                        help='输出目录（默认与源文件相同）')
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='显示详细编译输出')
    parser.add_argument('--clean', action='store_true',
                        help='编译后清理辅助文件')
    
    args = parser.parse_args()
    
    # 编译
    success = compile_latex(args.tex_file, args.output_dir, args.verbose)
    
    # 清理辅助文件
    if success and args.clean:
        print()
        clean_auxiliary_files(args.tex_file, args.output_dir)
    
    sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()
