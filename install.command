#!/bin/sh

sourcePath=$(dirname "${BASH_SOURCE[0]}")

sudo chmod -R +x ${sourcePath}/src
cat > ${sourcePath}/lips.sh <<EOF
#!/bin/bash
cd ${sourcePath}/src
python3 main.py \${@}
EOF

sudo rm /usr/local/bin/lips
sudo ln -s ${sourcePath}/lips.sh /usr/local/bin/lips

echo Added ip to /usr/local/bin

# Change permissions on the newly linked file
sudo chmod +x /usr/local/bin/lips
sudo chmod +x ${sourcePath}/uninstall.command
