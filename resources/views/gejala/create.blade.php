@extends('layout.main')
@section('content')
<div class="container mt-3">
    <div class="row justify-content-center align-items-center">
        <div class="card">
            <div class="card-header">Tambah Data Gejala
            </div>
            <div class="card-body">
                @if ($errors->any())
                <div class="alert alert-danger">
                    <strong>Whoops!</strong> There were some problems with your input.<br><br>
                    <ul>
                        @foreach ($errors->all() as $error)
                        <li>{{ $error }}</li>
                        @endforeach
                    </ul>
                </div>
                @endif
                <form method="post" action="/gejala" id="myForm" enctype="multipart/form-data">
                    @csrf
                    
                    <div style="margin-top:8px;">
                        <label>Kode Gejala</label>
                        <input type="text" class="w3-input w3-border w3-small" required name="kd_gejala"
                            value="" size="32">
                    </div>

                    <div style="margin-top:8px;">
                        <label>Gejala</label>
                        <input type="text" class="w3-input w3-border w3-small" required name="gejala"
                            value="" size="32">
                    </div>
                    <br>                    
                    <div class="w3-center">
                        <a onClick="window.history.back()" style="cursor:pointer"
                            class="w3-btn w3-small w3-red"><i class="fa fa-times-rectangle fa-fw"></i>
                            Batal</a> <button type="submit" class="w3-btn w3-small w3-green"><i
                                class="fa fa-save fa-fw"></i> Simpan</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</div>
@endsection