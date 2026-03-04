#!/bin/bash

echo "=== CET 활성화 확인 스크립트 ==="

echo -e "\n[1] CPU CET 지원 여부 확인:"
if grep -E -i 'cet_ibt|cet_ss' /proc/cpuinfo > /dev/null; then
    grep -m1 -o -E 'cet_ibt|cet_ss' /proc/cpuinfo | while read flag; do
        echo "  ✅ CPU는 $flag 플래그를 지원합니다."
    done
else
    echo "  ❌ CPU가 CET(IBT/SS)를 지원하지 않음"
fi

echo -e "\n[2] 커널이 CET 지원 플래그 인식 중인지 확인 (lscpu):"
lscpu | grep -i cet

echo -e "\n[3] 유저랜드 바이너리에서 endbr64 존재 여부 확인:"
TARGET="${1:-/bin/ls}"  # 기본 검사 대상: /bin/ls

if command -v objdump > /dev/null; then
    echo "  🔍 검사 대상: $TARGET"
    if objdump -d "$TARGET" | grep -q 'endbr64'; then
        echo "  ✅ $TARGET 바이너리에 endbr64 명령어 존재"
    else
        echo "  ❌ $TARGET 바이너리에 endbr64 명령어 없음"
    fi
else
    echo "  ⚠️ objdump 명령어가 설치되어 있지 않음"
fi

echo -e "\n[4] .note.gnu.property 섹션에서 CET 프로퍼티 확인:"
if command -v readelf > /dev/null; then
    if readelf -n "$TARGET" | grep -q 'GNU_PROPERTY_X86_FEATURE_1_IBT'; then
        echo "  ✅ $TARGET 바이너리에 IBT 속성 포함됨"
    else
        echo "  ❌ $TARGET 바이너리에 IBT 속성 없음"
    fi
else
    echo "  ⚠️ readelf 명령어가 설치되어 있지 않음"
fi

echo -e "\n✅ 검사 완료"

