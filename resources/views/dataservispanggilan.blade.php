@extends('layout.main')

@section('content')                      
    <!-- Begin Page Content -->
    <div class="container-fluid">

        <!-- Page Heading -->
        <h1 class="h3 mb-2 text-gray-800">Data Servis Panggilan</h1>
        <p class="mb-4">Berikut adalah daftar servis Panggilan</p>

      @if(Session::has('berhasil'))
          <div class="alert alert-success">
              <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button>
              <strong>Success,</strong>
              {{ Session::get('berhasil') }}
          </div>
      @endif
        <!-- DataTales Example -->
        <div class="card shadow mb-4">
          <div class="card-body">
            <div class="table-responsive">
              <table class="table table-bordered" id="dataTable" width="100%" cellspacing="0">
                <thead>
                  <tr>
                    <th>Id Servis Panggilan</th>
                    <th>Nomor HP</th>
                    <th>Lokaksi</th>

                  </tr>
                </thead>
                <tbody>
                  
                  @foreach ($servis_panggilan as $servisnya)
                  <tr>
                    <td>{{$servisnya->id}}</td>
                    <td>{{$servisnya->nope}}</td>
                    <td>{{$servisnya->lokasi}}</td>
   
                  </tr>
                  @endforeach
                </tbody>
              </table>
              {!!@$servis_panggilan->links()!!}
            </div>
          </div>
        </div>
      </div>
      <!-- /.container-fluid -->

       
@endsection