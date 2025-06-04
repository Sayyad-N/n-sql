#!/bin/bash

banner() {
cat << "EOF"

▗▄▄▄▖▄▄▄▄   ▄▄▄  ■  ▗▞▀▜▌█ █     ▗▖   ▄ ▗▖    ▄▄▄ 
  █  █   █ ▀▄▄▗▄▟▙▄▖▝▚▄▟▌█ █     ▐▌   ▄ ▐▌   ▀▄▄  
  █  █   █ ▄▄▄▀ ▐▌       █ █     ▐▌   █ ▐▛▀▚▖▄▄▄▀ 
▗▄█▄▖           ▐▌       █ █     ▐▙▄▄▖█ ▐▙▄▞▘     
                ▐▌                                
                                                  
                                                  
▗▄▄▖ ▄   ▄      ▗▄▄▖▗▞▀▜▌▄   ▄ ▄   ▄ ▗▞▀▜▌▐▌▗▖  ▗▖
▐▌ ▐▌█   █     ▐▌   ▝▚▄▟▌█   █ █   █ ▝▚▄▟▌▐▌▐▛▚▖▐▌
▐▛▀▚▖ ▀▀▀█      ▝▀▚▖      ▀▀▀█  ▀▀▀█   ▗▞▀▜▌▐▌ ▝▜▌
▐▙▄▞▘▄   █     ▗▄▄▞▘     ▄   █ ▄   █   ▝▚▄▟▌▐▌  ▐▌
      ▀▀▀                 ▀▀▀   ▀▀▀               
                                                  
EOF
}

run_fix_pip() {
    echo "⚠️ محاولة تصليح pip تلقائياً ..."
    if ! command -v expect >/dev/null 2>&1; then
        echo "تثبيت expect ..."
        if command -v apt >/dev/null 2>&1; then
            sudo apt update && sudo apt install -y expect
        elif command -v yum >/dev/null 2>&1; then
            sudo yum install -y expect
        elif command -v dnf >/dev/null 2>&1; then
            sudo dnf install -y expect
        elif command -v pacman >/dev/null 2>&1; then
            sudo pacman -Sy --noconfirm expect
        else
            echo "⚠️ لا يمكن تثبيت expect تلقائياً. رجاءً ثبت expect يدوياً."
            exit 1
        fi
    fi

    tmpdir=$(mktemp -d)
    git clone https://github.com/Sayyad-N/fix-pip.git "$tmpdir/fix-pip"
    cd "$tmpdir/fix-pip" || exit 1

    expect -c '
        spawn bash fix-pip.sh
        expect "Choose an option:"
        send "5\r"
        expect eof
    '

    cd - >/dev/null || exit 1
    rm -rf "$tmpdir"
    echo "✅ تم تصليح pip."
}

install_debian() {
    echo "✅ تحديث الحزم لـ Debian/Ubuntu ..."
    sudo apt update -y
    sudo apt install -y python3 python3-pip git expect
}

install_redhat() {
    echo "✅ تحديث الحزم لـ RedHat/CentOS/Fedora ..."
    sudo yum update -y || sudo dnf update -y
    sudo yum install -y python3 python3-pip git expect || sudo dnf install -y python3 python3-pip git expect
}

install_arch() {
    echo "✅ تحديث الحزم لـ Arch Linux ..."
    sudo pacman -Sy --noconfirm python python-pip git expect
}

install_dependencies() {
    if command -v apt >/dev/null 2>&1; then
        install_debian
    elif command -v yum >/dev/null 2>&1 || command -v dnf >/dev/null 2>&1; then
        install_redhat
    elif command -v pacman >/dev/null 2>&1; then
        install_arch
    else
        echo "⚠️ توزيعة غير مدعومة تلقائيًا. من فضلك ثبت python3, pip, git, expect يدويًا."
        exit 1
    fi

    # تأكد إن python يشير لـ python3
    if ! command -v python >/dev/null 2>&1; then
        echo "📎 python غير موجود، جاري ربطه بـ python3 ..."
        sudo ln -s /usr/bin/python3 /usr/bin/python
        echo "✅ تم إنشاء alias: python => python3"
    else
        PYTHON_VERSION=$(python -c "import sys; print(sys.version_info.major)")
        if [ "$PYTHON_VERSION" -ne 3 ]; then
            echo "⚠️ python الحالي ليس Python 3. سيتم ربطه بـ python3 بدلاً منه..."
            sudo rm -f /usr/bin/python
            sudo ln -s /usr/bin/python3 /usr/bin/python
            echo "✅ تم تحديث alias: python => python3"
        else
            echo "✅ python موجود وبيستخدم Python 3"
        fi
    fi

    echo "✅ تثبيت مكتبات Python المطلوبة..."
    if ! pip3 install --upgrade pip; then
        run_fix_pip
        pip3 install --upgrade pip
    fi

    if ! pip3 install requests urllib3; then
        run_fix_pip
        pip3 install requests urllib3
    fi
}

clone_sqlmap() {
    echo "✅ تنزيل أو تحديث sqlmap من GitHub..."
    if [ -d "sqlmap" ]; then
        cd sqlmap && git pull && cd ..
    else
        git clone --depth=1 https://github.com/sqlmapproject/sqlmap.git
    fi

    chmod +x sqlmap/sqlmap.py
}

main() {
    clear
    banner
    install_dependencies
    clone_sqlmap

    echo
    echo "🎉 تم الانتهاء من التثبيت بنجاح!"
    echo "✅ لتشغيل sqlmap من أي مكان:"
    echo "cd $(pwd)/sqlmap && python sqlmap.py -u 'http://target.com/vuln.php?id=1' --batch"
    echo
}

main

